import Image from "next/image";
import fs from "fs";
import { redirect } from "next/navigation";

export default function Home() {

  redirect("/overview");

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex"></div>
    </main>
  );
}
