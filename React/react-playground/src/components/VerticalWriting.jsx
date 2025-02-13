import styled from "styled-components"
import React from "react"

const StyledP = styled.p`
    writing-mode: vertical-lr
`

const VerticalWriting = (props) => {
    return <StyledP>{props.children}</StyledP>
}

export default VerticalWriting;
