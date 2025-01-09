import App from "../src/App";
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

it('should say React!', () => {
    render(<App/>);

    const appElement = screen.getByText("React!")

    expect(appElement).toBeInTheDocument()
});

it('should click button', () => {
    render(<App/>);

    const buttonElement = screen.getByRole('button', { name: /Thing Doer/i })
    fireEvent.click(buttonElement)

    expect(buttonElement).toHaveTextContent(/Thing Done/i)
});