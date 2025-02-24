async function fetchRandomUserData() {
    const apiUrl = 'https://randomuser.me/api/';
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        const user = data.results[0];
        const name = `${user.name.first} ${user.name.last}`;
        const email = user.email;
        return { name, email };
    } catch (error) {
        console.error('Error fetching user data:', error);
        return null;
    }
}
async function displayUserData() {
    const userData = await fetchRandomUserData();
    if (userData) {
        console.log('User Name:', userData.name);
        console.log('User Email:', userData.email);
    } else {
        console.log('Failed to fetch user data.');
    }
}
displayUserData();






function fetchRandomUserDataPromise() {
    const apiUrl = 'https://randomuser.me/api/';
    return fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const user = data.results[0];
            const name = `${user.name.first} ${user.name.last}`;
            const email = user.email;
            return { name, email };
        })
        .catch(error => {
            return null;
        });
}
function displayUserDataPromise() {
    fetchRandomUserDataPromise()
        .then(userData => {
            if (userData) {
                console.log('User Name:', userData.name);
                console.log('User Email:', userData.email);
            } else {
                console.log('Failed to fetch user data.');
            }
        });
}
displayUserDataPromise();