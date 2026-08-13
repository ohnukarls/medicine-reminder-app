export default function Dashboard() {
    return (
        <main className="min-h-screen bg-slate-50">
            <nav className="border-b border-slate-200 bg-white">
                <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
                    <h1 className="text-xl font-bold text-slate-900">
                        MediRem
                    </h1>

                    <div className="flex items-center gap-6">
                        <span className="text-sm font-medium text-slate-600">
                            Dashboard
                        </span>

                        <button className="text-sm font-medium text-slate-600 hover:text-slate-900">
                            Logout
                        </button>
                    </div>
                </div>
            </nav>

            <div className="mx-auto max-w-6xl px-6 py-10">
                <section>
                    <h2 className="text-3xl font-bold text-slate-900">
                        Good evening 👋
                    </h2>

                    <p className="mt-2 text-slate-600">
                        Here's what's happening with your medications today.
                    </p>
                </section>

                <section className="mt-8 grid gap-5 md:grid-cols-3">
                    <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
                        <p className="text-sm font-medium text-slate-500">
                            Medications
                        </p>

                        <p className="mt-2 text-3xl font-bold text-slate-900">
                            4
                        </p>
                    </div>

                    <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
                        <p className="text-sm font-medium text-slate-500">
                            Today's doses
                        </p>

                        <p className="mt-2 text-3xl font-bold text-slate-900">
                            6
                        </p>
                    </div>

                    <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
                        <p className="text-sm font-medium text-slate-500">
                            Adherence
                        </p>

                        <p className="mt-2 text-3xl font-bold text-slate-900">
                            92%
                        </p>
                    </div>
                </section>

                <section className="mt-10">
                    <h3 className="text-xl font-semibold text-slate-900">
                        Today's medications
                    </h3>

                    <div className="mt-4 overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
                        <div className="flex items-center justify-between border-b border-slate-100 p-5">
                            <div>
                                <p className="font-medium text-slate-900">
                                    Ibuprofen
                                </p>

                                <p className="mt-1 text-sm text-slate-500">
                                    400mg
                                </p>
                            </div>

                            <div className="flex items-center gap-6">
                                <span className="text-sm text-slate-500">
                                    08:00
                                </span>

                                <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
                                    Taken
                                </span>
                            </div>
                        </div>

                        <div className="flex items-center justify-between border-b border-slate-100 p-5">
                            <div>
                                <p className="font-medium text-slate-900">
                                    Vitamin D
                                </p>

                                <p className="mt-1 text-sm text-slate-500">
                                    1000 IU
                                </p>
                            </div>

                            <div className="flex items-center gap-6">
                                <span className="text-sm text-slate-500">
                                    12:00
                                </span>

                                <span className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
                                    Upcoming
                                </span>
                            </div>
                        </div>

                        <div className="flex items-center justify-between p-5">
                            <div>
                                <p className="font-medium text-slate-900">
                                    Metformin
                                </p>

                                <p className="mt-1 text-sm text-slate-500">
                                    500mg
                                </p>
                            </div>

                            <div className="flex items-center gap-6">
                                <span className="text-sm text-slate-500">
                                    20:00
                                </span>

                                <span className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
                                    Upcoming
                                </span>
                            </div>
                        </div>
                    </div>
                </section>

                <section className="mt-10">
                    <h3 className="text-xl font-semibold text-slate-900">
                        Upcoming reminders
                    </h3>

                    <div className="mt-4 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
                        <p className="text-sm font-medium text-slate-500">
                            Tomorrow
                        </p>

                        <div className="mt-4 space-y-4">
                            <div className="flex items-center justify-between">
                                <span className="text-sm text-slate-500">
                                    08:00
                                </span>

                                <span className="font-medium text-slate-900">
                                    Vitamin D
                                </span>
                            </div>

                            <div className="flex items-center justify-between">
                                <span className="text-sm text-slate-500">
                                    20:00
                                </span>

                                <span className="font-medium text-slate-900">
                                    Metformin
                                </span>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </main>
    );
}