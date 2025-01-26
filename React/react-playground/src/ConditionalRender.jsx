import React, { useCallback, useState } from "react";

const ConditionalRender = () => {
  const [show, setShow] = useState(true);

  const clickHandler = useCallback(() => {
    setShow(!show);
  }, [show, setShow]);

  return (
    <>
      {show && <h1>THis is the conditrionnal rednere</h1>}
      <button onClick={clickHandler}>{ show ? "Hide" : "Show"}</button>
    </>
  );
};

export default ConditionalRender;
