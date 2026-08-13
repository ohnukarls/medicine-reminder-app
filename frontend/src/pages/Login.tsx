import LoginForm from "../components/LoginForm/LoginForm";
import { Link } from "react-router-dom";
import { motion } from "motion/react";

export default function Login() {
    return (
        <main className="min-h-screen bg-slate-50 flex items-center justify-center">
            <motion.section
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -30 }}
              transition={{ duration: 0.3 }}
              className="bg-white p-8 rounded-xl shadow-sm">
                <h1 className="text-3xl font-bold text-slate-900">Welcome back</h1>
                
                <p className="mt-2 text-slate-600">
                    Sign in to manage your medications
                </p>
                
                <LoginForm/>
                
                <p className="mt-6 text-sm text-slate-600">
                    Don't have an account?{" "}
                    <Link
                        to="/register"
                        className="font-medium text-blue-600 hover:text-blue-700"
                    >
                        Sign up
                    </Link>
                </p>
            </motion.section>
        </main>
    );
}