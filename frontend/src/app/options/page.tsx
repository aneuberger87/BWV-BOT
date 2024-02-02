import { json } from "./options.example.json";

export default function Home() {
  const options = json;

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        Nils Angelika Jonas
      </div>
      {options.map((option) => (
        <div
          key={option.id}
          className="flex flex-col items-center justify-center"
        >
          <div className="text-2xl">{option.name}</div>
        </div>
      ))}
    </main>
  );
}
