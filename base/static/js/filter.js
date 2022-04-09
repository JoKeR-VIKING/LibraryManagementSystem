function filterBooks(allBooks)
{
    let filterBy = -1;
    let checkOne = document.getElementsByClassName('bookid')[0];
    let checkTwo = document.getElementsByClassName('category')[0];

    if (checkOne.value !== "")
    {
        filterBy = 0;
    }
    else if (checkTwo.value !== "Select Category")
    {
        filterBy = 1;
    }

    let dropdown = document.getElementsByClassName('filtered-menu')[0];
    dropdown.innerHTML = ""

    let defaultOption = document.createElement('option');
    defaultOption.hidden = true;
    defaultOption.disabled = true;
    defaultOption.selected = true;
    defaultOption.textContent = "Select book you want";

    dropdown.appendChild(defaultOption);

    for (let i=0;i<allBooks.length;i++)
    {
        let opt = document.createElement('option');
        opt.value = allBooks[i][0];
        opt.textContent += allBooks[i][1];

        if (filterBy === 0 && allBooks[i][0] !== checkOne.value)
            continue;
        if (filterBy === 1 && allBooks[i][2] !== checkTwo.value)
            continue;

        dropdown.appendChild(opt);
    }
}
