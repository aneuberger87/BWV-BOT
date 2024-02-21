import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

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
        <main className="m-auto p-20 h-full">{children}</main>
      </body>
    </html>
  );
}
