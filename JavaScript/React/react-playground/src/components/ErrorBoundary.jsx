import React from "react";

class ErrorBoundary extends React.Component {
    state = { hasError: false };

    componentDidCatch(error, info) {
        this.setState({ hasError: true })
    }

    render() {
        if (this.state.hasError) {
            return <h1>An error occurred! :D</h1>
        }
        return this.props.children
    }
}

export default ErrorBoundary;