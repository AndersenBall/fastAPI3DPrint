

const createUser = async (form,event) => {
    event.preventDefault();

    const apiUrl = 'http://127.0.0.1:8000/userAuthent/newUser'; 
    
    const userData = {
        fullName: form.elements.fullName.value,
        fullAddress: form.elements.fullAddress.value,
        username: form.elements.username.value,
        password: form.elements.password.value,
        email: form.elements.email.value,
        phoneNumber: form.elements.phoneNumber.value
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
            window.alert(`${errorData.detail}`);
        } else {
            window.alert('User creation success. You may now log in.');
            form.reset()
        }
    } catch (error) {
        window.alert(error.message);
    }
    return false;
};

const login = async (form,event) => {
    event.preventDefault();

    const apiUrl = 'http://127.0.0.1:8000/userAuthent/login'; 
    
    const userData = {
        username: form.elements.username.value,
        password: form.elements.password.value,
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
            window.alert(`${errorData.detail}`);
        } else {
            localStorage.setItem("username",form.elements.username.value);
            window.alert('Login Successful.');
            form.reset()
        }
    } catch (error) {
        window.alert(error.message);
    }
    return false;
};
//also need to pass in the name of the stl file. 
const addToCart = async (form, event, technology, infill, layerThickness, material, quantity) => {
    event.preventDefault();

    // Access the values passed as parameters
    const message = `Technology: ${technology}\nInfill: ${infill}\nLayer Thickness: ${layerThickness}\nMaterial: ${material}\nQuantity: ${quantity}`;

    //call backend api with these fields. It returns a price. Take price display it on subtotal. We will have shipping and setup be constant.

    window.alert(message);

    return true;
};


//pass in payment info
const confirmPayment = async (form, event) => {
    event.preventDefault();

    // Access the values passed as parameters
    const message = `Technology: ${technology}\nInfill: ${infill}\nLayer Thickness: ${layerThickness}\nMaterial: ${material}\nQuantity: ${quantity}`;

    //call function to actually make payment 
    window.alert(message);

    return true;
};