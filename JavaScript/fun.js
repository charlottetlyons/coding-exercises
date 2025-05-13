async function sleep() {
    await new Promise(r => setTimeout(r, 1000));
}

function createH1() {
    return document.createElement("h1");
}

function fetchPost(url, body) {
    fetch(url, {
        method: "POST",
        body: JSON.stringify(body),
        headers: {}
    })
}

function reverse_words(string) {
    return string.split(' ').reverse().join(" ")
}

function countOccurrences(string, char) {
    count = 0;
    for (let i = 0; i < string.length; i++) {
        if (string[i] == char) {
            count ++;
        }
    }
    return count
}

async function asyncFunction(func) {
    try {
        await func()
    } catch (error) {
        // 
    }
}