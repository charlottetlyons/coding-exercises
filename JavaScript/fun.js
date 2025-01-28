async function sleep() {
    await new Promise(r => setTimeout(r, 1000));
}

function createH1() {
    return document.createElement("h1");
}

sleep()