import React from "react";

const Form = () => {
  return (
    <form action={() => console.log("love <3")}>
      <label>Label</label>
      <input></input>
      <input type="submit" />
    </form>
  );
};

export default Form;
