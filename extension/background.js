chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    console.log("Received:", request);

    fetch("https://aishield-wq0t.onrender.com/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: request.text
        })
    })
    .then(response => {
        console.log("Status:", response.status);
        return response.json();
    })
    .then(data => {
        console.log("Data:", data);
        sendResponse(data);
    })
    .catch(error => {
        console.error(error);
        sendResponse({ error: error.message });
    });

    return true;
});