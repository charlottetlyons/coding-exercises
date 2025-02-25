import React, { useCallback, useState } from "react"

const Button = (props) => {
    const [text, setText] = useState(props.children) 
    
    const clickHandler = useCallback(() => {
        setText(text == "Thing Doer" ? "Thing Done" : "Thing Doer")
    }, [text, setText])

    return <button onClick={clickHandler}>{text}</button>
}

export default Button;