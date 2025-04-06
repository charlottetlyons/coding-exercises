import React from "react"
import styled from "styled-components";

// x y blur spread color
const StyledBlurredEdgeComponent = styled.div`
    box-shadow: 10px -10px 10px 10px black;
    height: 100px;
    width: 100px;
    background-color: green;
`

const BlurredEdgesElement = () => {
    return <StyledBlurredEdgeComponent />
}

export default BlurredEdgesElement;