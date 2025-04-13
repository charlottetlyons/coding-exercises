const { useState } = require("react")
const { useCallback } = require("react")

const useInputValidation = () => {
    const validate = useCallback((value) => {
        console.log(value == "text")
    }, [])

    return {
        validate
    }
}

export default useInputValidation;