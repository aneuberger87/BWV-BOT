import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";

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
        <TooltipProvider>
          <main className="m-auto h-full max-w-7xl p-10">
            {children}
            <Toaster />
          </main>
        </TooltipProvider>
      </body>
    </html>
  );
}
