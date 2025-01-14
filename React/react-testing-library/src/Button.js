import React, { useState, useCallback } from "react"

const Button = () => {
    const [buttonText, setButtonText] = useState("Thing Doer")

    const buttonClickHandler = useCallback(() => {
        setButtonText("Thing Done");
    }, [setButtonText]);

    return <button onClick={buttonClickHandler}>{buttonText}</button>
}

export default Button;