# Get Lyrics

Simple Python scripts that aid in retrieving any song lyrics using the Genius API
or the currently playing song on Spotify.

For example to display the currently playing spotify song and display it with less:
```
./spotify-song | ./get-lyrics | less
```

## Setting up the get-lyrics script
In order to use this you need to get a genius client access token that can
be generated [Here](https://genius.com/api-clients/new). Then you need to set an
environment variable of `GENIUS_CLIENT_TOKEN` equal to the client access token,
to make this persistent put it in your `.bashrc`
