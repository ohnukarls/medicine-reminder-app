import { useState } from "react";
import Input from "../Input/Input";
import Button from "../Button/Button";
import { register } from "../../api/auth";

export default function RegisterForm() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        
        try {
            await register({ username, email, password });
            console.log("User registered successfully");
        } catch (error) {
            console.error("Error registering user:", error);
        }
    };

    return (
        <form
            onSubmit={handleSubmit}
            className="mt-8 space-y-5"
        >
            <div className="flex flex-col gap-2">
                <label
                    htmlFor="username"
                    className="text-sm font-medium text-slate-700"
                >
                    Username
                </label>

                <Input
                    id="username"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
            </div>

            <div className="flex flex-col gap-2">
                <label
                    htmlFor="email"
                    className="text-sm font-medium text-slate-700"
                >
                    Email
                </label>

                <Input
                    id="email"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>

            <div className="flex flex-col gap-2">
                <label
                    htmlFor="password"
                    className="text-sm font-medium text-slate-700"
                >
                    Password
                </label>

                <Input
                    id="password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>

            <Button type="submit">
                Register
            </Button>
        </form>
    );
}