import React from 'react';
import './Navbar.css';
import { faHome, faSearch, faUsers, faComments, faBell, faUser, faBars } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

function Navbar() {
    return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
            <a className="navbar-brand" href="#">ConnMe</a>
            <div className="search justify-content-center">
                <input type="text" className="search-box"/>
                <span className="search-button">
                    <FontAwesomeIcon icon={faSearch} />
                </span>
            </div>
            <div className="hamburger">
                <button>
                    <FontAwesomeIcon icon={faBars} />
                </button>
            </div>
            <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="#">
                            <FontAwesomeIcon icon={faHome} />
                        </a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="#">
                            <FontAwesomeIcon icon={faUsers} />
                        </a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="#">
                            <FontAwesomeIcon icon={faComments} />
                        </a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="#">
                            <FontAwesomeIcon icon={faBell} />
                        </a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link active" aria-current="page" href="#">
                            <FontAwesomeIcon icon={faUser} />
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    )
}

export default Navbar;
