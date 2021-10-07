function deletePlaylistItem(playlistItemId) {
    fetch("/delete-playlist-item", {
        method: "POST",
        body: JSON.stringify({ playlistItemId: playlistItemId }),
    }).then((_res) => {
        window.location.href = "/app";
    });
}


function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.

    var auth2 = gapi.auth2.getAuthInstance();
    auth2.disconnect();

    fetch('/google_sign_in', {
        method: "POST",
        body: JSON.stringify({ id_token: id_token }),
        headers: {
            "content-type": "application/json"
        }
    }).then((_res) => {
        console.log(_res);
        console.log('js login success');
        window.location.href = "/app";
    });
    // $.ajax({
    //     type: "POST",
    //     url: '/google_sign_in',
    //     data: JSON.stringify({ 'id_token': id_token }),
    //     success: function () {
    //         console.log('login success')
    //         window.location.href = "/app";
    //     },
    //     dataType: 'json',
    //     contentType: "application/json",
    // });
}


if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}