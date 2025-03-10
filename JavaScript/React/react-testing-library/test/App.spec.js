import App from "../src/App";
import { render, screen } from '@testing-library/react';
import React from 'react';

it("should say React!", () => {
    render(<App/>);

    const appElement = screen.getByText(/React!/);

    expect(appElement).toBeInTheDocument();
});