async function processComment(element) {

    if (element.dataset.aishieldProcessed) return;

    element.dataset.aishieldProcessed = "true";

    const text = element.innerText.trim();

    if (!text) return;

    const result = await predictComment(text);

    if (!result) return;

    console.log(text, result);

    if (result.prediction === "Spam") {
        highlightSpam(element, result.confidence);
    }
}