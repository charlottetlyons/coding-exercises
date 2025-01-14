async function sleep() {
    await new Promise(r => setTimeout(r, 1000));
}

sleep()