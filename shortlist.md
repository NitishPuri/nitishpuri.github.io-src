* aboutwilson
<!-- * basic -->
* bootstrap
<!-- * built-texts -->
<!-- * photowall -->
* flex
<!-- * hyde -->
<!-- * svbhack -->
* fresh

### Plugins
* https://github.com/getpelican/pelican-plugins
* https://github.com/getpelican/pelican-plugins/tree/master/autopages
* https://github.com/getpelican/pelican-plugins/tree/master/goodreads_activity
* https://github.com/getpelican/pelican-plugins/tree/master/gravatar
* https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags
* https://github.com/mortada/pelican_javascript/tree/58e7335e5f5fa0acc945425c2d12bf9dcadb150f


## IPython tools
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

%matplotlib inline
%config InlineBackend.figure_format='retina'
%config IPCompleter.greedy=True
```

## Capture screen
```sh
ffmpeg -list_devices true -f dshow -i dummy
ffmpeg -f dshow -i video="screen-capture-recorder" output.flv
ffmpeg -f dshow -i audio="virtual-audio-capturer":video="screen-capture-recorder" yo.mp4
ffmpeg -video_size 1920x1080 -framerate 30 -f x11grab -i :0.0 -c:v libx264 -qp 0 -preset ultrafast capture.mkv
ffmpeg -f dshow -i video="screen-capture-recorder" -c:v libx264 -qp 0 output2.flv
```