loadListing = async function () {
    const brokenImageElement = document.createElement("img");
    brokenImageElement.src = brokenImagePath;
    brokenImageElement.classList.add("broken-image");
    console.log(`this file will try to load listing ${listingId}`);
    listingApiUrl = apiBaseUrl + "/listings/" + listingId + "/combined";
    console.log(`Trying to fetch from ${listingApiUrl}`);

    let listingData = await fetch(listingApiUrl)
        .then(response => {
            if (response.ok) {
                console.log("response", response);
                return response.json();
            }
            throw new Error("Error in response");
        })
        .then(body => {
            return body;
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    console.log("listingData", listingData);

    // Update page title
    document.title = listingData.name + " - " + document.title;

    // Update page contents
    // Listing Name
    listingName = document.querySelectorAll(".listing-name-insert");
    listingName.forEach(element => {
        element.innerText = listingData.name;
    });

    // Listing Agent
    listingAgent = document.querySelectorAll(".listing-agent-insert");
    listingAgent.forEach(element => {
        element.innerText = listingData.agent;
    });


    // Listing Company
    listingCompany = document.querySelectorAll(".listing-company-insert");
    listingCompany.forEach(element => {
        element.innerText = listingData.company;
    });

    // Listing Price
    listingPrice = document.querySelectorAll(".listing-price-insert");
    listingPrice.forEach(element => {
        element.innerText = listingData.price;
    });

    // Listing Location
    listingLocation = document.querySelectorAll(".listing-location-insert");
    listingLocation.forEach(element => {
        element.innerText = listingData.location;
    });


    // Listing Description
    listingDescription = document.querySelectorAll(".listing-description-insert");
    listingDescription.forEach(element => {
        element.innerText = listingData.description;
    });


    // Listing Category
    listingCategory = document.querySelectorAll(".listing-category-insert");
    listingCategory.forEach(element => {
        element.innerText = listingData.category;
    });

    // Listing Status
    listingStatus = document.querySelectorAll(".listing-status-insert");
    listingStatus.forEach(element => {
        if (listingData.status) {
            element.innerText = listingData.status;
        }
        else {
            element.classList.add("empty-property");
        }
    });


    // Listing Rooms
    listingRooms = document.querySelectorAll(".listing-rooms-insert");
    listingRooms.forEach(element => {
        if (listingData.rooms) {
            element.innerText = listingData.rooms;
        }
        else {
            element.classList.add("empty-property");
        }
    });


    // Listing Area
    listingArea = document.querySelectorAll(".listing-area-insert");
    listingArea.forEach(element => {
        if (listingData.area) {
            element.innerText = listingData.area;
        }
        else {
            element.classList.add("empty-property");
        }
    });

    // Listing Floors
    listingFloors = document.querySelectorAll(".listing-floors-insert");
    listingFloors.forEach(element => {
        if (listingData.floors) {
            element.innerText = listingData.floors;
        }
        else {
            element.classList.add("empty-property");
        }
    });


    // Listing Energy Class
    listingEnergyClass = document.querySelectorAll(".listing-energy-class-insert");
    listingEnergyClass.forEach(element => {
        if (listingData.energyClass) {
            element.innerText = listingData.energyClass;
        }
        else {
            element.classList.add("empty-property");
        }
    });

    // Listing Upkeep
    listingUpkeep = document.querySelectorAll(".listing-upkeep-insert");
    listingUpkeep.forEach(element => {
        if (listingData.upkeep) {
            element.innerText = listingData.upkeep;
        }
        else {
            element.classList.add("empty-property");
        }
    });

    // Listing Year
    listingYear = document.querySelectorAll(".listing-year-insert");
    listingYear.forEach(element => {
        if (listingData.year) {
            element.innerText = listingData.year;
        }
        else {
            element.classList.add("empty-property");
        }
    });

    // Listing Entity
    listingEntity = document.querySelectorAll(".listing-entity-insert");
    listingEntity.forEach(element => {
        if (listingData.entity) {
            element.innerText = listingData.entity;
        }
        else {
            element.classList.add("empty-property");
        }
    });


    // Listing Agent Image
    if (listingData.image_user_id) {
        // console.log("load image?");
        listingAgentImage = document.querySelectorAll(".listing-agent-image");
        const userImageUrl = apiBaseUrl + "/users/" + listingData.image_user_id + "/image";
        const imageElement = document.createElement("img");
        fetch(userImageUrl)
            .then(response => response.blob())
            .then(blob => {
                const objectUrl = URL.createObjectURL(blob);
                imageElement.src = objectUrl;
                listingAgentImage.forEach(element => {
                    element.appendChild(imageElement);
                });
            })
            .catch(error => {
                console.error('Error fetching the image:', error);
            });
        // console.log("got this", objectUrl);
    }
    listingImagesContainer = document.querySelector(".listing-images")
    const listingImageUrl = apiBaseUrl + "/listings/" + listingId + "/images";
    listingImages = await fetch(listingImageUrl)
        .then(response => {
            if (response.ok) {
                console.log("response", response);
                return response.json();
            }
            throw new Error("Error in response");
        })
        .then(body => {
            return body;
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    console.log("listingImages", listingImages);
    if (listingImages.length) {
        console.log("got images");
        listingImages.forEach(listingImage => {
            let listingImageUrl = apiBaseUrl + "/listings/images/" + listingImage.image_id;
            console.log(listingImageUrl);
            let imageElement = document.createElement("img");
            fetch(listingImageUrl)
                .then(response => response.blob())
                .then(blob => {
                    const objectUrl = URL.createObjectURL(blob);
                    imageElement.src = objectUrl;
                    listingImagesContainer.appendChild(imageElement);
                })
                .catch(error => {
                    console.error('Error fetching the image:', error);
                });

        });
    }
    else {
        console.log("no images");
        listingImagesContainer.appendChild(brokenImageElement);
    }


};