async function sleep() {
    console.log("Start")
    await new Promise(r => setTimeout(r, 5000))
    console.log("End")
}

sleep()