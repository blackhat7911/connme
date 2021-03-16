import React from 'react';
import AppIllustration from '../assets/images/social-media.png';

function Login() {

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-8">
                    <img className="image" src={AppIllustration} alt=""/>
                </div>
                <div className="col-md-4">
                    <div className="form">
                        <div className="mb-3">
                            <label for="username" className="form-label">Username</label>
                            <input type="text" 
                                className="form-control" 
                                id="username"  
                                placeholder="name" 
                                />
                        </div>
                        <div className="mb-3">
                            <label for="password" className="form-label">Password</label>
                            <input 
                                type="password" 
                                className="form-control" 
                                id="password" 
                                placeholder="password" 
                                />
                        </div>
                        <button 
                            type="submit" 
                            class="btn btn-primary mb-3"
                            >
                            Login
                            </button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Login
