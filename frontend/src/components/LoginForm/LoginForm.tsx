import { useState } from 'react';
import Input from '../Input/Input';
import Button from '../Button/Button';
import { login } from "../../api/auth";
import { useAuth } from '../../contexts/AuthContext';

export default function LoginForm() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { login: saveToken } = useAuth();

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        try {
            const response = await login({ email, password });
            console.log("User logged in successfully");
            saveToken(response.access_token);
        } catch (error) {
            console.error("Error logging in user:", error);
        }
    };

  return (
        <form
            onSubmit={handleSubmit}
            className="mt-8 space-y-5"
        >
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
                Sign In
            </Button>
        </form>
    );
}