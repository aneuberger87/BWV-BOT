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
      <body className={inter.className + " h-full w-full"}>
        <main className="max-w-xl m-auto">{children}</main>
      </body>
    </html>
  );
}
