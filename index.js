function getVideoURL() {
  const params = {
      title: document.getElementById('titleInput').value
  };
  const options = {
      method: 'POST',
      body: JSON.stringify( params )  ,
      headers: {
        'Content-Type': 'application/json'
      }
  };
  fetch( '/download', options )
      .then( response => response.json() )
      .then( response => {
          alert(response.downloadVideoUrl)
      } );
  location.reload();
}

