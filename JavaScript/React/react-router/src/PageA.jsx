import React from 'react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const PageA = () => {
    const navigate = useNavigate();

    useEffect(() => {
        setTimeout(() => {
            navigate('/page-b');
        }, 3000);
    }, [navigate]);

    return (
        <div>
            <h1>Page A</h1>
        </div>
    );
};

export default PageA;