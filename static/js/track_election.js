console.log("Tracking election")

const  electionId = document.getElementById('election_id').innerText.trim()


const socket = new WebSocket(
    `ws://${window.location.host}/ws/dev-stories/dc/${electionId}/`
    )



socket.onmessage = function(e) {
    console.log("Server: " + e.data)
};

socket.onopen = function(e) {

    socket.send(JSON.stringify({
        'voter': '6df49a9f-2afd-458d-ae9c-71c4a91052f6',
        'party': '2'
    }));
};