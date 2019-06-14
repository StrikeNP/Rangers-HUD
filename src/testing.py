import sys
import spotipy
import spotipy.util as util
from pynput.keyboard import Key, Controller, Listener

SPOTIPY_CLIENT_ID='af93d78862ad47bcbbcc14a7f9712a60'
SPOTIPY_CLIENT_SECRET='2e498f3cc02a4e65801c27fd20168ca3'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
USERNAME="USERNAME"

scope = 'user-modify-playback-state'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

if token:
    # sp.pause_playback()
    keyboard = Controller()

def on_press(key):
    print('{0} pressed'.format(key))
    if key.char == 'p':
        print("Pausing playback")
        sp.pause_playback()
    if key.char == 's':
        print("Starting playback")
        sp.start_playback()


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    # client = spotipy.client.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)