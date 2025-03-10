import Button from "../src/Button";
import { render, screen, fireEvent } from "@testing-library/react";
import React from "react";

it("should click button", () => {
  render(<Button>Thing Doer</Button>);

  const buttonElement = screen.getByRole("button", { name: /Thing Doer/i });
  fireEvent.click(buttonElement);

  expect(buttonElement).toHaveTextContent(/Thing Done/i);
});
