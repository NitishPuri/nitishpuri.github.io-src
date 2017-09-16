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
Date: {year}-{month}-{day}
gallery: {photo}{title}
"""

gallery_post_template = """
Title: {title}
Date: {year}-{month}-{day}

![{caption}]({photo}/{gallery}/{filename})
"""

def generate_gallery_pages():
    settings = read_settings('pelicanconf.py')
    photo_lib_path = settings['PHOTO_LIBRARY']
    # print(photo_lib_path)
    import  glob 

    # Cleanup..
    galleries = 'content/art/auto_*.md'
    art_pages = 'content/pages/auto_*.md'
    for gal in glob.iglob(galleries):
        print("Removing file,.. {}".format(gal))
        os.remove(gal)

    for art in glob.iglob(art_pages):
        print("Removing file,... {}".format(art))
        os.remove(art)

    if(os.path.isdir(photo_lib_path)):
        for gallery in sorted(os.listdir(photo_lib_path)):
            # Generate Gallery article
            galleryPath = os.path.join(photo_lib_path, gallery)


            mtime = datetime.fromtimestamp(os.path.getmtime(galleryPath))            

            gt = album_template.strip().format(title= gallery,
                                          year = mtime.year,
                                          month = mtime.month,
                                          day = mtime.day,
                                          photo='{photo}'
            )

            g_create = 'content/art/auto_{}_{:0>2}_{:0>2}_{}.md'.format(
                mtime.year, mtime.month, mtime.day, gallery) 

            with open(g_create, 'w') as w:
                w.write(gt)
            print("File created -> " + g_create)

            for pic in sorted(os.listdir(galleryPath)):

                picPath = os.path.join(galleryPath, pic)
                pmtime = datetime.fromtimestamp(os.path.getmtime(picPath))

                picName = pic.split('.')[0]

                pt = gallery_post_template.strip().format(title=picName,
                                                          year=pmtime.year,
                                                          month=pmtime.month,
                                                          day=pmtime.day,
                                                          caption='ssdhgf',
                                                          photo='{photo}',
                                                          gallery=gallery,
                                                          filename=pic)

                p_create = 'content/pages/auto_{}_{:0>2}_{:0>2}_{}.md'.format(
                    pmtime.year, pmtime.month, pmtime.day, picName)

                with open(p_create, 'w') as w:
                    w.write(pt)
                print("File created -> " + p_create)
            

