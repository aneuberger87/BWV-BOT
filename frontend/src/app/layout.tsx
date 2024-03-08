import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/sonner"

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "bwv-bot",
  description: "Nils Angelika Jonas",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full w-full">
      <body className={inter.className + " h-full w-full bg-background"}>
        <main className="m-auto p-10 max-w-7xl h-full">{children}
        <Toaster />
        </main>
      </body>
    </html>
  );
}
