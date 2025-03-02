import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      {/* Hero Section */}
      <header className="bg-blue-600 text-white text-center py-12">
        <h1 className="text-4xl font-bold">Welcome to Hackathon Connect</h1>
        <p className="mt-2 text-lg">
          Find teammates, track hackathons, and collaborate seamlessly!
        </p>
      </header>

      {/* Search Bar */}
      <div className="flex justify-center mt-6">
        <input
          type="text"
          placeholder="Search for hackathons..."
          className="w-1/2 p-2 border rounded-lg"
        />
      </div>

      {/* Quick Links */}
      <div className="grid grid-cols-3 gap-4 text-center mt-8 px-10">
        <Link
          to="/profile"
          className="bg-white p-6 rounded-xl shadow hover:bg-blue-100"
        >
          <h2 className="text-xl font-semibold">Profile</h2>
          <p>Customize your profile and showcase your skills</p>
        </Link>
        <Link
          to="/matchmaking"
          className="bg-white p-6 rounded-xl shadow hover:bg-blue-100"
        >
          <h2 className="text-xl font-semibold">Matchmaking</h2>
          <p>Find compatible teammates for your next hackathon</p>
        </Link>
        <Link
          to="/team-dashboard"
          className="bg-white p-6 rounded-xl shadow hover:bg-blue-100"
        >
          <h2 className="text-xl font-semibold">Team Dashboard</h2>
          <p>Manage tasks, collaborate, and track progress</p>
        </Link>
      </div>

      {/* Featured Hackathons */}
      <section className="mt-10 px-10">
        <h2 className="text-2xl font-semibold">Upcoming Hackathons</h2>
        <div className="grid grid-cols-3 gap-4 mt-4">
          {/* Sample Hackathon Cards */}
          <div className="bg-white p-4 rounded-xl shadow">
            <h3 className="font-semibold text-lg">AI Innovation Hack</h3>
            <p>Date: March 10, 2025</p>
            <p>Prize: $10,000</p>
          </div>
          <div className="bg-white p-4 rounded-xl shadow">
            <h3 className="font-semibold text-lg">HealthTech Challenge</h3>
            <p>Date: April 5, 2025</p>
            <p>Prize: $8,000</p>
          </div>
          <div className="bg-white p-4 rounded-xl shadow">
            <h3 className="font-semibold text-lg">Blockchain Build</h3>
            <p>Date: April 20, 2025</p>
            <p>Prize: $12,000</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
