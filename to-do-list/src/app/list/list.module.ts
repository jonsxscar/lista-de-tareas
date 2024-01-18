import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TareaListaComponent } from '../tarea-lista/tarea-lista.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [TareaListaComponent],
  imports: [CommonModule, FormsModule],
  exports: [TareaListaComponent]
})
export class TareaListaModule { }