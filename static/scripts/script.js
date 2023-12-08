const createUser = async () => {
    const apiUrl = 'http://127.0.0.1:8000/userAuthent/newUser'; 
    
    const userData = {
        fullName: 'John Doe',
        fullAddress: '123 Main St, Cityville',
        username: 'john_doe',
        password: 'secretpassword',
        email: 'john.doe@example.com',
        phoneNumber: '123-456-7890'
    };

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        });

        if (!response.ok) {
            // Handle non 2xx responses
            const errorData = await response.json();
            window.alert(`Error: ${response.status} - ${errorData.detail}`);
        } else {
            const responseData = await response.json();
            window.alert(`Success: ${JSON.stringify(responseData)}`);
        }
    } catch (error) {
        window.alert(`Error: ${error.message}`);
    }
};
