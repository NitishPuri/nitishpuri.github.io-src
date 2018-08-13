

# Render a bunch of images into a movie file
# activate RoboND
# set IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\convert.exe"

import moviepy.editor as mp


def seqToVideo(images, videoPath):
    clip = mp.ImageSequenceClip(images, fps=1/5)
    print(clip)
    clip.write_videofile(videoPath)


def gifToVideo(gifPath, videoPath):
    clip = mp.VideoFileClip(gifPath)
    print(clip)
    clip.write_videofile(videoPath)


def concatVideo(input1, input2, output):
    video1 = mp.VideoFileClip(input1)
    video2 = mp.VideoFileClip(input2)
    concat = mp.concatenate_videoclips([video1, video2])
    concat.write_videofile(output)


if __name__ == "__main__":
    print("Here??")
    # gifToVideo('D:/tree/insta/gif/12.gif', 'D:/tree/insta/gif/12.mp4')
    seqToVideo('D:/tree/insta/gif', 'D:/tree/insta/12.mp4')

# def


# input_video = "world1_edited.mp4"
# input_video1 = "vid/followMe/2.mp4"
# input_video2 = "vid/followMe/1.mp4"
# output_video = 'concat.mp4'

# concatVideo(input_video1, input_video2, output_video)


# Make the text. Many more options are available.
# txt_clip = ( TextClip("This is a test.",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10) )

# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video

# result = video.speedx(factor=2.0)
# result.write_videofile("world1_fast.mp4") # Many options...
