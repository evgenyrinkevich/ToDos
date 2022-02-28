import React from "react";

const items = [
    {
        "name": "ToDos",
        href: "#"
    },
    {
        "name": "About",
        href: "#"
    },
    {
        "name": "Main Page",
        href: "#"
    }
]


const MenuItem = ({item}) => {
    return (
        <li key={item.name}>
            <a href={item.href}>{item.name}</a>
        </li>
    )
}

const Menu = () => {
    return (
        <div className="menu">
            <ul>
                {items.map((item) => <MenuItem item={item} />)}
            </ul>
        </div>
    )
}

export default Menu