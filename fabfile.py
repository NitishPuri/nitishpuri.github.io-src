from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

from datetime import datetime

from pelican.server import ComplexHTTPRequestHandler
from pelican.settings import read_settings

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# # Rackspace Cloud Files configuration settings
# env.cloudfiles_username = 'my_rackspace_username'
# env.cloudfiles_api_key = 'my_rackspace_api_key'
# env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "master"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    import glob
    if os.path.isdir(DEPLOY_PATH):
        for folder in glob.iglob(DEPLOY_PATH + '/*'):
            print(folder)
            if(os.path.isdir(folder)):
                shutil.rmtree(folder)
            else:
                os.remove(folder)

        # shutil.rmtree(DEPLOY_PATH)
        # os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`build` with the delete switch"""
    local('pelican -d -s pelicanconf.py')

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def livereload():
    """ build and then serve using livereload server"""
    build()
    local("python pelican-livereload.py")

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

# def cf_upload():
#     """Publish to Rackspace Cloud Files"""
#     rebuild()
#     with lcd(DEPLOY_PATH):
#         local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#               '-U {cloudfiles_username} '
#               '-K {cloudfiles_api_key} '
#               'upload -c {cloudfiles_container} .'.format(**env))


TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Tags:
Category:
Slug: {slug}
Summary:
Status: draft


"""

# TEMPLATE is declared before hand, and all the necessary imports made
def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

# def gh_pages():
#     """Publish to GitHub Pages"""
#     rebuild()
#     local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))

def testTask(testVar="nothing"):
    print("You passed {} as argument.".format(testVar))

def gh_push(commitMsg = "Update"):
    """Push to Github Pages"""
    rebuild()

    # Push the blog 
    local("cd output")
    local("git add --all")
    local("git commit -m '{}'".format(commitMsg))
    local("git push -u origin master")

    # Push source
    local("cd ..")
    local("git add .")
    local("git commit -m '{}'".format(commitMsg))
    local("git push -u origin master")

def clone_output():
    local("git clone https://github.com/nitishpuri/nitishpuri.github.io.git output")


def optimize_images():
    """ Resize photos to optimize for web."""
    from PIL import Image
    import glob

    path = 'content/images/papers/*.png'
    for file in glob.iglob(path):
        # print(file)
        img = Image.open(file)
        bg = Image.new('RGB', img.size, (255, 255, 255))
        # img = img.split()[0:3]
        bg.paste(img, img)
        newfile = file[0:-3]
        newfile += '.jpg'
        print("{} --> {}".format(file, newfile))
        bg.save(newfile, 'JPEG', quality=90)
    


album_template = """
Title: {title}
Date: {date}
gallery: {photo}{title}
tags: {tag}
summary: {desc}

{desc}

"""

gallery_page_template = """
Title: Gallery
date: 10-10-2017
gallery: {gallery}
comments: enabled
"""

gallery_post_template = """
Title: {title}
Date: {year}-{month}-{day}
comments: enabled

#### {desc}
![{caption}]({photo}/{gallery}/{filename})
"""

def get_proper_timestamp(path):
    if os.path.isfile(path) == False:
        return datetime.today()
    
    try:        
        ts = os.path.getmtime(path)
        return datetime.fromtimestamp(ts)
    except:
        ts = os.path.getctime(path)
        return datetime.fromtimestamp(ts)


def generate_gallery():
    import json
    # gallery_json = 'gallery.json'
    settings = read_settings('pelicanconf.py')

    photo_lib_path = settings['PHOTO_LIBRARY']
    gallery_json = settings['PHOTO_JSON']

    # photo_lib_path = "gallery"

    with open(gallery_json) as data_file:
        gallery_data = json.load(data_file)

    # print(photo_lib_path)
    import  glob 

    # Delete previously auto generated pages.
    galleries = 'content/gallery/auto_*.md'
    for gal in glob.iglob(galleries):
        print("Removing file,.. {}".format(gal))
        os.remove(gal)

    art_pages = 'content/pages/auto_*.md'
    for art in glob.iglob(art_pages):
        print("Removing file,... {}".format(art))
        os.remove(art)

    gallery_page = 'content/pages/auto_gallery.md'
    if(os.path.isfile(gallery_page)):
        os.remove(gallery_page)
        print("Removing file,... {}".format(gallery_page))

    gallery_str = ''

    # Cleanup Photos directory 
    if os.path.isdir(photo_lib_path):
        print("Cleaning up photos directory")
        shutil.rmtree(photo_lib_path, ignore_errors=True)

    os.makedirs(photo_lib_path)

    gallery_root = gallery_data['root_path']
    print("Gallery Root : {}".format(gallery_root))

    # Copy photos to photo directory
    for gallery in gallery_data['galleries']:
        galleryName = gallery['name']

        galleryPath = os.path.join(photo_lib_path, galleryName)
        print("Creating dir,.. {}".format(galleryPath))
        os.makedirs(galleryPath)

        gt = album_template.strip().format(title=galleryName,
                                           date=gallery['date'],
                                           tag=gallery['tag'],
                                           desc=gallery['desc'],
                                           photo='{photo}')

        gallery_str += '{photo}' + galleryName + '{' + galleryName+'},'

        g_create = 'content/gallery/auto_{}.md'.format(galleryName) 
        with open(g_create, 'w') as w:
            w.write(gt)
        print("File created -> " + g_create)

        for file in gallery['files']:            
            fileSourcePath = os.path.join(gallery_root, file)
            fileName = os.path.basename(fileSourcePath)
            fileDestPath = os.path.join(galleryPath, fileName)

            file_desc = gallery['files'][file]

            fileStrippedName = fileName.split('.')[0]

            pmtime = get_proper_timestamp(fileSourcePath)

            if os.path.isfile(fileDestPath) == False:
                print('Copying file to : {}'.format(fileDestPath))
                shutil.copyfile(fileSourcePath, fileDestPath)
            else:
                print("File already exists at : {}".format(fileDestPath))

            pt = gallery_post_template.strip().format(title=fileStrippedName,
                                                     year = pmtime.year,
                                                     month=pmtime.month,
                                                     day=pmtime.day,
                                                     caption=fileStrippedName,
                                                     photo='{photo}',
                                                     gallery=galleryName,
                                                     filename=fileName,
                                                     desc=file_desc)

            p_create = 'content/pages/auto_{}_{:0>2}_{:0>2}_{}.md'.format(
                pmtime.year, pmtime.month, pmtime.day, fileStrippedName)

            with open(p_create, 'w') as w:
                w.write(pt)
            print("File created -> " + p_create)

            
    gallery_str = gallery_str[0:-1] # remove trailing comma
    gallery_t = gallery_page_template.strip().format(gallery=gallery_str)
    with open(gallery_page, 'w') as w:
        w.write(gallery_t)
    print("File created -> " + gallery_page)


def test_json():
    from pprint import pprint

    settings = read_settings('pelicanconf.py')
    photo_lib_path = settings['PHOTO_LIBRARY']

    gallery_json = 'gallery/gallery.json'

    with open(gallery_json) as data_file:
        data = json.load(data_file)
    
    pprint(data['galleries'][0])



def renameImages():
    import glob
    from PIL import Image
    INPUT_IMAGES = 'D:\Google Drive\Art\RandomSessions\{file}.{format}'
    for file in glob.iglob(INPUT_IMAGES.strip().format(file='*', format='png')):
        fileName = os.path.basename(file).split('.')[0]
        newName = INPUT_IMAGES.strip().format(file=fileName, format='jpg')
        # while os.path.isfile(newName) :
        #     index += 1
        #     newName = '../test_data2/g/{}.jpg'.format(index)

        print("{} --> {}".format(file, newName))        

        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(newName)
