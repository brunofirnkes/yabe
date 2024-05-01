import React, { useState } from 'react'; // Import useState hook
import { useNavigate } from 'react-router-dom'; // Import useNavigate hook
import "../styles/Navbar.css";
import logo from ".././logo.png"

function Navbar() {
    const [search, setSearch] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSearch = async (e) => {
        setLoading(true);
        e.preventDefault();
        console.log({ search });
    };

    return (
        <div className='navbar-base'>
            <img src={logo} alt="logo" className='navbar-logo'/>
            <form onSubmit={handleSearch} className="navbar-search">
                <input
                    className="navbar-searchInput"
                    type="text"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="Search for anything"
                />
                <button className="navbar-searchButton" type="submit">
                    Search
                </button>
            </form>
        </div>
    );
}

export default Navbar;