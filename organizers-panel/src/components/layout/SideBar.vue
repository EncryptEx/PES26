<template>
    <aside class="w-64 flex-shrink-0 border-r border-white/10 bg-background-dark flex flex-col justify-between">
                <div class="p-6">
                    <div class="flex items-center gap-3 mb-10">
                        <div
                            class="h-10 w-10 rounded-xl bg-gradient-to-br from-primary to-accent-pink flex items-center justify-center">
                            <span
                                class="material-symbols-outlined text-background-dark font-bold">celebration</span>
                        </div>
                        <div>
                            <h1
                                class="text-xl font-bold tracking-tighter text-white">GRESCA</h1>
                            <p
                                class="text-[10px] uppercase tracking-widest text-primary font-bold">Organizer
                                Portal</p>
                        </div>
                    </div>
                    <nav class="space-y-2">
                        <a
                            class="flex items-center gap-3 px-4 py-3 rounded-xl bg-primary/10 text-primary border border-primary/20"
                            href="#">
                            <span
                                class="material-symbols-outlined">dashboard</span>
                            <span class="text-sm font-semibold">Dashboard</span>
                        </a>
                        <a
                            class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:bg-white/5 hover:text-white transition-all"
                            href="#">
                            <span
                                class="material-symbols-outlined">confirmation_number</span>
                            <span class="text-sm font-medium">My Parties</span>
                        </a>
                        <a
                            class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:bg-white/5 hover:text-white transition-all"
                            href="#">
                            <span
                                class="material-symbols-outlined">add_circle</span>
                            <span class="text-sm font-medium">Create
                                Party</span>
                        </a>
                        <a
                            class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:bg-white/5 hover:text-white transition-all"
                            href="#">
                            <span
                                class="material-symbols-outlined">monitoring</span>
                            <span class="text-sm font-medium">Analytics</span>
                        </a>
                        <a
                            class="flex items-center gap-3 px-4 py-3 rounded-xl text-slate-400 hover:bg-white/5 hover:text-white transition-all"
                            href="#">
                            <span
                                class="material-symbols-outlined">settings</span>
                            <span class="text-sm font-medium">Settings</span>
                        </a>
                    </nav>
                </div>
                <!-- Mini Profile Footer -->
                <div class="p-4 m-4 glass rounded-2xl flex items-center gap-3">
                    <img
                        class="h-10 w-10 rounded-full object-cover border-2 border-primary/30"
                        data-alt="Profile photo of a professional organizer"
                        src="https://lh3.googleusercontent.com/aida-public/AB6AXuCnaOmwkkdfFO29JiuaRKky3mvgPSlFUk3CkyWeIqdFyBEI77agOqe7PC288dYIHSanV89Yepq548Rp_UE8esJCKEsYPkROjwIFpyBlPq8XMYNM8Wak0bK7gOYKWrbLQ-cFdH1d8wZciAh_bB45l6_YbbZezRaWTcYBDDSHNQEzvBSodI8l8nAS23GUZM4_AZbHX9cAJ0NRRyRU1rPynczmvPmapuWLSoW3xwEPsHHHts3ihV3zoc0UQLEs3Pgj_z_bRKno8fJqYvey" />
                    <div class="flex-1 overflow-hidden">
                        <p class="text-sm font-bold truncate text-white">Alex
                            Rivera</p>
                        <button
                            class="text-[10px] text-primary hover:text-primary/80 uppercase font-bold tracking-tight">Edit
                            Profile</button>
                    </div>
                    <button
                        class="text-slate-500 hover:text-accent-pink transition-colors">
                        <span
                            class="material-symbols-outlined text-lg">logout</span>
                    </button>
                </div>
            </aside>
</template>