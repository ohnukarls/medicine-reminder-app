import RegisterForm from "../components/RegisterForm/RegisterForm";
import { Link } from "react-router-dom";
import { motion } from "motion/react";

export default function Register() {
    return (
        <main className="min-h-screen bg-slate-50 flex items-center justify-center px-4">
            <motion.section
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -30 }}
              transition={{ duration: 0.3 }}
              className="w-full max-w-md bg-white p-8 rounded-xl shadow-sm"
            >
                <h1 className="text-3xl font-bold text-slate-900">
                    Create your account
                </h1>

                <p className="mt-2 text-slate-600">
                    Create an account to start managing your medications.
                </p>

                <RegisterForm />

                <p className="mt-6 text-sm text-slate-600 text-center">
                    Already have an account?{" "}
                    <Link
                        to="/login"
                        className="font-medium text-blue-600 hover:text-blue-700"
                    >
                        Sign in
                    </Link>
                </p>
            </motion.section>
        </main>
    );
}