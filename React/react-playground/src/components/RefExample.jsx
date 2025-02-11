import React, { useCallback, useRef } from "react";

const RefExample = () => {
    const reference = useRef('');

    const refLog = useCallback(() => {
        console.log(reference.current?.value)
    }, [reference])

    return <>
        <input ref={reference} type="text"/>
        <button onClick={refLog}>Log</button>
    </>
};

export default RefExample;