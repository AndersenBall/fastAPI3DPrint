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
            const errorData = await response.json();
            sessionStorage.setItem("username", form.elements.username.value)
            window.alert('Login Successful.');
            form.reset()
        }
    } catch (error) {
        window.alert(error.message);
    }
    return false;
};

const uploadSTL = async (form, event) => {
    event.preventDefault();

    const apiUrl = 'http://127.0.0.1:8000/uploadfile'; 

    const formData = new FormData();
    formData.append('file', form.elements.fileInput.files[0])

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            // Handle non 2xx responses
            const errorData = await response.json();
            window.alert(`Failed to Upload Image. Try again.`);
        } else {
            const responseData = await response.json();
            sessionStorage.setItem("stlFile", form.elements.fileInput.files[0].name)
            window.alert('File Uploaded: ' + sessionStorage.getItem("stlFile"));
        }
    } catch (error) {
        window.alert(error.message);
    }
    return false;
};

//also need to pass in the name of the stl file. 
const addToCart = async() => {
    //Get values from dropdowns
    const apiUrl = 'http://127.0.0.1:8000/checkout/newOrder';
    const checkoutData = {
        modelName: sessionStorage.getItem("stlFile"),
        tech: document.getElementById("technology").value,
        infil: document.getElementById("infill").value,
        layerthick: document.getElementById("layerThickness").value,
        material: document.getElementById("material").value,
        userName: sessionStorage.getItem("username"),
    };

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(checkoutData),
        });

        if (!response.ok) {
            // Handle non 2xx responses
            const errorData = await response.json();
            window.alert(`${errorData.detail}`);
        } else {
            getFileCost();
            window.alert('Successfully Added to Cart');
        }
    } catch (error) {
        window.alert(error.message);
    }
};

async function getFileCost(filename) {
    const apiUrl = `https://your-api-domain.com/calcfileCost/${filename}`;

    try {
        const response = await fetch(apiUrl);

        if (!response.ok) {
            throw new Error(`Error - Status: ${response.status}`);
        }
        else
            costData = await response.json();
            cost = JSON.parse(costData).cost;
            document.getElementById("subtotal").testContent = string('$' + cost);
    } catch (error) {
        console.error('Error fetching file cost:', error.message);
        return null;
    }
}


//pass in payment info
const confirmPayment = async (form, event) => {
    event.preventDefault();

    // Access the values passed as parameters
    const message = `Technology: ${technology}\nInfill: ${infill}\nLayer Thickness: ${layerThickness}\nMaterial: ${material}\nQuantity: ${quantity}`;

    //call function to actually make payment 
    window.alert(message);

    return true;
};

