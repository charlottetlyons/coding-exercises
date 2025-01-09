import React, { useCallback, useState } from "react"

const App = () => {
    const [buttonText, setButtonText] = useState("Thing Doer")

    const buttonClickHandler = useCallback(() => {
        setButtonText("Thing Done");
    }, [setButtonText]);

    return <div>
        <h1>React!</h1>
        <button onClick={buttonClickHandler}>{buttonText}</button>
    </div>
}
export default App;