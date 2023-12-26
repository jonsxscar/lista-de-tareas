import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'tarea-lista',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './tarea-lista.component.html',
  styleUrl: './tarea-lista.component.css',
})
export class TareaListaComponent {
  tareas = [
    { nombre: 'Tarea 1', completada: false },
    { nombre: 'Tarea 2', completada: true },
    { nombre: 'Tarea 3', completada: false },
  ];
  nuevaTarea = '';

  agregarTarea() {
    if (this.nuevaTarea) {
      this.tareas.push({ nombre: this.nuevaTarea, completada: false });
      this.nuevaTarea = '';
    }
  }

  eliminarTarea(index: number) {
    this.tareas.splice(index, 1);
  }
}
