import React from "react";
import styled from "styled-components";

const StyledParallaxDiv = styled.div`
    background: linear-gradient(217deg, rgba(255, 0, 0, 0.8), rgba(255, 0, 0, 0) 70.71%), linear-gradient(127deg, rgba(0, 255, 0, 0.8), rgba(0, 255, 0, 0) 70.71%), linear-gradient(336deg, rgba(0, 0, 255, 0.8), rgba(0, 0, 255, 0) 70.71%);
    background-size: cover;
    background-attachment: fixed;
    height: 100vh;
`

const ParallaxComponent = () => {
    return <StyledParallaxDiv>
    </StyledParallaxDiv>
}

export default ParallaxComponent;